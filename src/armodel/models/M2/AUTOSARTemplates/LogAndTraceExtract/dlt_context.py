"""DltContext AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # context
        "context_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # contextId
        "dlt_messages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltMessage,
        ),  # dltMessages
    }

    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_messages: list[DltMessage] = []


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
