"""EcucDestinationUriPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucDestinationUriPolicy(ARObject):
    """AUTOSAR EcucDestinationUriPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("containers", None, False, True, EcucContainerDef),  # containers
        ("destination_uri", None, False, False, any (EcucDestinationUri)),  # destinationUri
        ("parameters", None, False, True, EcucParameterDef),  # parameters
        ("references", None, False, True, any (EcucAbstractReference)),  # references
    ]

    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.references: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucDestinationUriPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriPolicy":
        """Create EcucDestinationUriPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucDestinationUriPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucDestinationUriPolicy since parent returns ARObject
        return cast("EcucDestinationUriPolicy", obj)


class EcucDestinationUriPolicyBuilder:
    """Builder for EcucDestinationUriPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriPolicy = EcucDestinationUriPolicy()

    def build(self) -> EcucDestinationUriPolicy:
        """Build and return EcucDestinationUriPolicy object.

        Returns:
            EcucDestinationUriPolicy instance
        """
        # TODO: Add validation
        return self._obj
