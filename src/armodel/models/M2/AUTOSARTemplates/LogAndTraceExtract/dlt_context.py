"""DltContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 9)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context: Optional[String]
    context_id: Optional[String]
    dlt_messages: list[DltMessage]
    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_messages: list[DltMessage] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltContext":
        """Deserialize XML element to DltContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltContext object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = child.text
            obj.context = context_value

        # Parse context_id
        child = ARObject._find_child_element(element, "CONTEXT-ID")
        if child is not None:
            context_id_value = child.text
            obj.context_id = context_id_value

        # Parse dlt_messages (list)
        obj.dlt_messages = []
        for child in ARObject._find_all_child_elements(element, "DLT-MESSAGES"):
            dlt_messages_value = ARObject._deserialize_by_tag(child, "DltMessage")
            obj.dlt_messages.append(dlt_messages_value)

        return obj



class DltContextBuilder:
    """Builder for DltContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltContext = DltContext()

    def build(self) -> DltContext:
        """Build and return DltContext object.

        Returns:
            DltContext instance
        """
        # TODO: Add validation
        return self._obj
