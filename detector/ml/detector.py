"""Demo ML detector. It is trained on generated sample data, not a real platform dataset."""
from functools import lru_cache
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

FEATURES = ["followers", "following", "posts", "account_age_days", "bio_length", "has_profile_picture", "posts_per_day", "follower_following_ratio"]

@lru_cache(maxsize=1)
def get_model_and_metrics():
    rng = np.random.default_rng(4311)
    n = 2400
    age = rng.integers(1, 4000, n)
    followers = np.maximum(0, rng.lognormal(4.7, 1.2, n).astype(int))
    following = np.maximum(0, rng.lognormal(4.8, 1.0, n).astype(int))
    posts = np.maximum(0, rng.lognormal(3.4, 1.0, n).astype(int))
    bio = rng.integers(0, 180, n)
    picture = rng.integers(0, 2, n)
    rate = posts / np.maximum(age, 1)
    ratio = followers / np.maximum(following, 1)
    # Labels are generated from a transparent illustrative heuristic to make a runnable demo dataset.
    fake_probability = (age < 45).astype(float) * .22 + (picture == 0).astype(float) * .18 + (rate > 2.5).astype(float) * .18 + (ratio < .15).astype(float) * .20 + (bio < 8).astype(float) * .12 + (following > followers * 8).astype(float) * .18
    fake_probability += rng.normal(0, .12, n)
    y = (fake_probability > .32).astype(int)
    X = np.column_stack([followers, following, posts, age, bio, picture, rate, ratio])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=160, max_depth=10, class_weight="balanced", random_state=42)
    model.fit(X_train, y_train)
    return model, accuracy_score(y_test, model.predict(X_test))

def predict_account(*, followers, following, posts, account_age_days, bio_length, has_profile_picture):
    age = max(int(account_age_days), 1)
    following = int(following)
    followers = int(followers)
    posts = int(posts)
    rate = posts / age
    ratio = followers / max(following, 1)
    row = np.array([[followers, following, posts, int(account_age_days), int(bio_length), int(bool(has_profile_picture)), rate, ratio]], dtype=float)
    model, validation_accuracy = get_model_and_metrics()
    probabilities = model.predict_proba(row)[0]
    fake_index = list(model.classes_).index(1)
    risk = float(probabilities[fake_index]) * 100
    label = "Fake" if risk >= 50 else "Real"
    return {"prediction": label, "risk_score": round(risk, 1), "validation_accuracy": round(validation_accuracy * 100, 1), "features": {"posts_per_day": round(rate, 3), "follower_following_ratio": round(ratio, 3)}}
