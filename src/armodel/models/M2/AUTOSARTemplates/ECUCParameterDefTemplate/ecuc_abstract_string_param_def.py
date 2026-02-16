"""EcucAbstractStringParamDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RegularExpression,
    VerbatimString,
)


class EcucAbstractStringParamDef(ARObject):
    """AUTOSAR EcucAbstractStringParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultValue
        "max_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxLength
        "min_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minLength
        "regular": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # regular
    }

    def __init__(self) -> None:
        """Initialize EcucAbstractStringParamDef."""
        super().__init__()
        self.default_value: Optional[VerbatimString] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min_length: Optional[PositiveInteger] = None
        self.regular: Optional[RegularExpression] = None


class EcucAbstractStringParamDefBuilder:
    """Builder for EcucAbstractStringParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractStringParamDef = EcucAbstractStringParamDef()

    def build(self) -> EcucAbstractStringParamDef:
        """Build and return EcucAbstractStringParamDef object.

        Returns:
            EcucAbstractStringParamDef instance
        """
        # TODO: Add validation
        return self._obj
