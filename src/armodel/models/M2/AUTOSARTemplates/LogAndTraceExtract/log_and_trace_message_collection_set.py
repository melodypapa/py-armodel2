"""LogAndTraceMessageCollectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class LogAndTraceMessageCollectionSet(ARElement):
    """AUTOSAR LogAndTraceMessageCollectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_messages: list[DltMessage]
    def __init__(self) -> None:
        """Initialize LogAndTraceMessageCollectionSet."""
        super().__init__()
        self.dlt_messages: list[DltMessage] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LogAndTraceMessageCollectionSet":
        """Deserialize XML element to LogAndTraceMessageCollectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LogAndTraceMessageCollectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LogAndTraceMessageCollectionSet, cls).deserialize(element)

        # Parse dlt_messages (list from container "DLT-MESSAGES")
        obj.dlt_messages = []
        container = ARObject._find_child_element(element, "DLT-MESSAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_messages.append(child_value)

        return obj



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
