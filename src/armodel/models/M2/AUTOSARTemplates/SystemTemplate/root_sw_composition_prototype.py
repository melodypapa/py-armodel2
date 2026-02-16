"""RootSwCompositionPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_map import (
    FlatMap,
)


class RootSwCompositionPrototype(Identifiable):
    """AUTOSAR RootSwCompositionPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("calibrations", None, False, True, any (CalibrationParameter)),  # calibrations
        ("flat_map", None, False, False, FlatMap),  # flatMap
        ("software", None, False, False, CompositionSwComponentType),  # software
    ]

    def __init__(self) -> None:
        """Initialize RootSwCompositionPrototype."""
        super().__init__()
        self.calibrations: list[Any] = []
        self.flat_map: Optional[FlatMap] = None
        self.software: Optional[CompositionSwComponentType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RootSwCompositionPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RootSwCompositionPrototype":
        """Create RootSwCompositionPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RootSwCompositionPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RootSwCompositionPrototype since parent returns ARObject
        return cast("RootSwCompositionPrototype", obj)


class RootSwCompositionPrototypeBuilder:
    """Builder for RootSwCompositionPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RootSwCompositionPrototype = RootSwCompositionPrototype()

    def build(self) -> RootSwCompositionPrototype:
        """Build and return RootSwCompositionPrototype object.

        Returns:
            RootSwCompositionPrototype instance
        """
        # TODO: Add validation
        return self._obj
