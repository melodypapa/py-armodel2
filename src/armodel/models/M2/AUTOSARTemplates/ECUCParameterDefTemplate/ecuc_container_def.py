"""EcucContainerDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)


class EcucContainerDef(EcucDefinitionElement):
    """AUTOSAR EcucContainerDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_uris", None, False, True, EcucDestinationUriDef),  # destinationUris
        ("multiplicities", None, False, True, EcucMultiplicityConfigurationClass),  # multiplicities
        ("origin", None, True, False, None),  # origin
        ("post_build_variant", None, True, False, None),  # postBuildVariant
        ("requires_index", None, True, False, None),  # requiresIndex
    ]

    def __init__(self) -> None:
        """Initialize EcucContainerDef."""
        super().__init__()
        self.destination_uris: list[EcucDestinationUriDef] = []
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucContainerDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerDef":
        """Create EcucContainerDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucContainerDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucContainerDef since parent returns ARObject
        return cast("EcucContainerDef", obj)


class EcucContainerDefBuilder:
    """Builder for EcucContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerDef = EcucContainerDef()

    def build(self) -> EcucContainerDef:
        """Build and return EcucContainerDef object.

        Returns:
            EcucContainerDef instance
        """
        # TODO: Add validation
        return self._obj
