"""BlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Generic.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)


class BlueprintMapping(ARObject):
    """AUTOSAR BlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint: AtpBlueprint
    derived_object: AtpBlueprintable
    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint: AtpBlueprint = None
        self.derived_object: AtpBlueprintable = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize blueprint
        if self.blueprint is not None:
            serialized = ARObject._serialize_item(self.blueprint, "AtpBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_object
        if self.derived_object is not None:
            serialized = ARObject._serialize_item(self.derived_object, "AtpBlueprintable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVED-OBJECT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintMapping":
        """Deserialize XML element to BlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint
        child = ARObject._find_child_element(element, "BLUEPRINT")
        if child is not None:
            blueprint_value = ARObject._deserialize_by_tag(child, "AtpBlueprint")
            obj.blueprint = blueprint_value

        # Parse derived_object
        child = ARObject._find_child_element(element, "DERIVED-OBJECT")
        if child is not None:
            derived_object_value = ARObject._deserialize_by_tag(child, "AtpBlueprintable")
            obj.derived_object = derived_object_value

        return obj



class BlueprintMappingBuilder:
    """Builder for BlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMapping = BlueprintMapping()

    def build(self) -> BlueprintMapping:
        """Build and return BlueprintMapping object.

        Returns:
            BlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
