from unittest.mock import Mock

import pytest

from domain import Reporter, Notifier, Application

@pytest.fixture
def reporter():
    instance = Reporter()
    instance.generate_report = Mock()
    instance.generate_report_value = "42"
    return instance

@pytest.fixture
def notifier():
    instance = Notifier()
    instance.notify = Mock()
    return instance


@pytest.fixture
def application(reporter, notifier):
    return Application(reporter, notifier)


def test_should_send_prepared_report(application):
    application.process()

    application._notifier.notify.assert_called_once_with("The following report has been generated: 42")