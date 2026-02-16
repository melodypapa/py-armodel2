"""EcucParameterDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)


class EcucParameterDef(EcucCommonAttributes):
    """AUTOSAR EcucParameterDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("derivation", None, False, False, EcucDerivationSpecification),  # derivation
        ("symbolic_name", None, True, False, None),  # symbolicName
        ("with_auto", None, True, False, None),  # withAuto
    ]

    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucParameterDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDef":
        """Create EcucParameterDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucParameterDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucParameterDef since parent returns ARObject
        return cast("EcucParameterDef", obj)


class EcucParameterDefBuilder:
    """Builder for EcucParameterDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDef = EcucParameterDef()

    def build(self) -> EcucParameterDef:
        """Build and return EcucParameterDef object.

        Returns:
            EcucParameterDef instance
        """
        # TODO: Add validation
        return self._obj
