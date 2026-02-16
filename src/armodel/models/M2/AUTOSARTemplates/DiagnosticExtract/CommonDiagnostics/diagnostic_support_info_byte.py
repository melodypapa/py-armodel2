"""DiagnosticSupportInfoByte AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticSupportInfoByte(ARObject):
    """AUTOSAR DiagnosticSupportInfoByte."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # position
        "size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # size
    }

    def __init__(self) -> None:
        """Initialize DiagnosticSupportInfoByte."""
        super().__init__()
        self.position: Optional[PositiveInteger] = None
        self.size: Optional[PositiveInteger] = None


class DiagnosticSupportInfoByteBuilder:
    """Builder for DiagnosticSupportInfoByte."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSupportInfoByte = DiagnosticSupportInfoByte()

    def build(self) -> DiagnosticSupportInfoByte:
        """Build and return DiagnosticSupportInfoByte object.

        Returns:
            DiagnosticSupportInfoByte instance
        """
        # TODO: Add validation
        return self._obj
