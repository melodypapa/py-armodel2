"""TransformationTechnology AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.buffer_properties import (
    BufferProperties,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)


class TransformationTechnology(Identifiable):
    """AUTOSAR TransformationTechnology."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("buffer_properties", None, False, False, BufferProperties),  # bufferProperties
        ("has_internal", None, True, False, None),  # hasInternal
        ("needs_original", None, True, False, None),  # needsOriginal
        ("protocol", None, True, False, None),  # protocol
        ("transformation_description", None, False, False, TransformationDescription),  # transformationDescription
        ("transformer", None, False, False, TransformerClassEnum),  # transformer
        ("version", None, True, False, None),  # version
    ]

    def __init__(self) -> None:
        """Initialize TransformationTechnology."""
        super().__init__()
        self.buffer_properties: Optional[BufferProperties] = None
        self.has_internal: Optional[Boolean] = None
        self.needs_original: Optional[Boolean] = None
        self.protocol: Optional[String] = None
        self.transformation_description: Optional[TransformationDescription] = None
        self.transformer: Optional[TransformerClassEnum] = None
        self.version: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransformationTechnology to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationTechnology":
        """Create TransformationTechnology from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransformationTechnology instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransformationTechnology since parent returns ARObject
        return cast("TransformationTechnology", obj)


class TransformationTechnologyBuilder:
    """Builder for TransformationTechnology."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationTechnology = TransformationTechnology()

    def build(self) -> TransformationTechnology:
        """Build and return TransformationTechnology object.

        Returns:
            TransformationTechnology instance
        """
        # TODO: Add validation
        return self._obj
