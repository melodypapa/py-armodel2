"""BlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Generic.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    blueprint_ref: ARRef
    derived_object_ref: ARRef
    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint_ref: ARRef = None
        self.derived_object_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_ref
        if self.blueprint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint_ref, "AtpBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_object_ref
        if self.derived_object_ref is not None:
            serialized = SerializationHelper.serialize_item(self.derived_object_ref, "AtpBlueprintable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVED-OBJECT-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintMapping, cls).deserialize(element)

        # Parse blueprint_ref
        child = SerializationHelper.find_child_element(element, "BLUEPRINT-REF")
        if child is not None:
            blueprint_ref_value = ARRef.deserialize(child)
            obj.blueprint_ref = blueprint_ref_value

        # Parse derived_object_ref
        child = SerializationHelper.find_child_element(element, "DERIVED-OBJECT-REF")
        if child is not None:
            derived_object_ref_value = ARRef.deserialize(child)
            obj.derived_object_ref = derived_object_ref_value

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
