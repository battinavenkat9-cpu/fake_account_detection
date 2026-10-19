from django.core.management.base import BaseCommand
from detector.ml.detector import get_model_and_metrics

class Command(BaseCommand):
    help = "Initialize and validate the demo fake-account classifier."
    def handle(self, *args, **options):
        _, accuracy = get_model_and_metrics()
        self.stdout.write(self.style.SUCCESS(f"Demo classifier trained successfully. Holdout accuracy on generated demo data: {accuracy:.1%}"))
        self.stdout.write("Note: this is synthetic demo data, not evidence of real-world detection accuracy.")
