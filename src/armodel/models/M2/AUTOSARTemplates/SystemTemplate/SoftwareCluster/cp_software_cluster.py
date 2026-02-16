"""CpSoftwareCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class CpSoftwareCluster(ARElement):
    """AUTOSAR CpSoftwareCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("software_cluster", None, True, False, None),  # softwareCluster
        ("sw_components", None, False, True, any (SwComponent)),  # swComponents
        ("sw_composition_component_types", None, False, True, CompositionSwComponentType),  # swCompositionComponentTypes
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareCluster."""
        super().__init__()
        self.software_cluster: Optional[PositiveInteger] = None
        self.sw_components: list[Any] = []
        self.sw_composition_component_types: list[CompositionSwComponentType] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareCluster":
        """Create CpSoftwareCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareCluster since parent returns ARObject
        return cast("CpSoftwareCluster", obj)


class CpSoftwareClusterBuilder:
    """Builder for CpSoftwareCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareCluster = CpSoftwareCluster()

    def build(self) -> CpSoftwareCluster:
        """Build and return CpSoftwareCluster object.

        Returns:
            CpSoftwareCluster instance
        """
        # TODO: Add validation
        return self._obj
