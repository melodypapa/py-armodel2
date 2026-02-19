"""TransformationTechnology AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 764)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformerClassEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    buffer_properties: Optional[BufferProperties]
    has_internal: Optional[Boolean]
    needs_original: Optional[Boolean]
    protocol: Optional[String]
    transformation_description: Optional[TransformationDescription]
    transformer: Optional[TransformerClassEnum]
    version: Optional[String]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationTechnology":
        """Deserialize XML element to TransformationTechnology object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationTechnology object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse buffer_properties
        child = ARObject._find_child_element(element, "BUFFER-PROPERTIES")
        if child is not None:
            buffer_properties_value = ARObject._deserialize_by_tag(child, "BufferProperties")
            obj.buffer_properties = buffer_properties_value

        # Parse has_internal
        child = ARObject._find_child_element(element, "HAS-INTERNAL")
        if child is not None:
            has_internal_value = child.text
            obj.has_internal = has_internal_value

        # Parse needs_original
        child = ARObject._find_child_element(element, "NEEDS-ORIGINAL")
        if child is not None:
            needs_original_value = child.text
            obj.needs_original = needs_original_value

        # Parse protocol
        child = ARObject._find_child_element(element, "PROTOCOL")
        if child is not None:
            protocol_value = child.text
            obj.protocol = protocol_value

        # Parse transformation_description
        child = ARObject._find_child_element(element, "TRANSFORMATION-DESCRIPTION")
        if child is not None:
            transformation_description_value = ARObject._deserialize_by_tag(child, "TransformationDescription")
            obj.transformation_description = transformation_description_value

        # Parse transformer
        child = ARObject._find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = child.text
            obj.transformer = transformer_value

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        return obj



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
