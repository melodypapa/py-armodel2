"""Collection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class Collection(ARElement):
    """AUTOSAR Collection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auto_collect_enum", None, False, False, AutoCollectEnum),  # autoCollectEnum
        ("collecteds", None, False, True, AtpFeature),  # collecteds
        ("collection", None, True, False, None),  # collection
        ("elements", None, False, True, Identifiable),  # elements
        ("element_role", None, True, False, None),  # elementRole
        ("source_elements", None, False, True, Identifiable),  # sourceElements
        ("source_instances", None, False, True, AtpFeature),  # sourceInstances
    ]

    def __init__(self) -> None:
        """Initialize Collection."""
        super().__init__()
        self.auto_collect_enum: Optional[AutoCollectEnum] = None
        self.collecteds: list[AtpFeature] = []
        self.collection: Optional[NameToken] = None
        self.elements: list[Identifiable] = []
        self.element_role: Optional[Identifier] = None
        self.source_elements: list[Identifiable] = []
        self.source_instances: list[AtpFeature] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Collection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Collection":
        """Create Collection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Collection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Collection since parent returns ARObject
        return cast("Collection", obj)


class CollectionBuilder:
    """Builder for Collection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Collection = Collection()

    def build(self) -> Collection:
        """Build and return Collection object.

        Returns:
            Collection instance
        """
        # TODO: Add validation
        return self._obj
