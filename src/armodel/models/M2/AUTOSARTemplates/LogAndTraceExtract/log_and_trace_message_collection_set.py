"""LogAndTraceMessageCollectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class LogAndTraceMessageCollectionSet(ARElement):
    """AUTOSAR LogAndTraceMessageCollectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dlt_messages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltMessage,
        ),  # dltMessages
    }

    def __init__(self) -> None:
        """Initialize LogAndTraceMessageCollectionSet."""
        super().__init__()
        self.dlt_messages: list[DltMessage] = []


class LogAndTraceMessageCollectionSetBuilder:
    """Builder for LogAndTraceMessageCollectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LogAndTraceMessageCollectionSet = LogAndTraceMessageCollectionSet()

    def build(self) -> LogAndTraceMessageCollectionSet:
        """Build and return LogAndTraceMessageCollectionSet object.

        Returns:
            LogAndTraceMessageCollectionSet instance
        """
        # TODO: Add validation
        return self._obj
