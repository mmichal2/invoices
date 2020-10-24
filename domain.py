class Reporter:
    def generate_report(self) -> str:
        pass


class Notifier:
    def notify(self, massage: str):
        pass


class Application:
    def __init__(self, reporter: Reporter, notifier: Notifier):
        self._reporter = reporter
        self._notifier = notifier

    def process(self):
        report = self._reporter.generate_report()
        self._notifier.notify(f"The following report has been generated: {report}")
