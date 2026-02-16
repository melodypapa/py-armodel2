"""EcucEnumerationLiteralDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecuc_cond": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucCondition),
        ),  # ecucCond
        "origin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # origin
    }

    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None


class EcucEnumerationLiteralDefBuilder:
    """Builder for EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()

    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return EcucEnumerationLiteralDef object.

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
