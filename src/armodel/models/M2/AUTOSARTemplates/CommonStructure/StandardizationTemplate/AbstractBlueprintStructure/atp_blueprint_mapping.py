"""AtpBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

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
from abc import ABC, abstractmethod


class AtpBlueprintMapping(ARObject, ABC):
    """AUTOSAR AtpBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_blueprint: AtpBlueprint
    atp_blueprinted: AtpBlueprintable
    def __init__(self) -> None:
        """Initialize AtpBlueprintMapping."""
        super().__init__()
        self.atp_blueprint: AtpBlueprint = None
        self.atp_blueprinted: AtpBlueprintable = None
    def serialize(self) -> ET.Element:
        """Serialize AtpBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize atp_blueprint
        if self.atp_blueprint is not None:
            serialized = ARObject._serialize_item(self.atp_blueprint, "AtpBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BLUEPRINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize atp_blueprinted
        if self.atp_blueprinted is not None:
            serialized = ARObject._serialize_item(self.atp_blueprinted, "AtpBlueprintable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BLUEPRINTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprintMapping":
        """Deserialize XML element to AtpBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpBlueprintMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse atp_blueprint
        child = ARObject._find_child_element(element, "ATP-BLUEPRINT")
        if child is not None:
            atp_blueprint_value = ARObject._deserialize_by_tag(child, "AtpBlueprint")
            obj.atp_blueprint = atp_blueprint_value

        # Parse atp_blueprinted
        child = ARObject._find_child_element(element, "ATP-BLUEPRINTED")
        if child is not None:
            atp_blueprinted_value = ARObject._deserialize_by_tag(child, "AtpBlueprintable")
            obj.atp_blueprinted = atp_blueprinted_value

        return obj



class AtpBlueprintMappingBuilder:
    """Builder for AtpBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprintMapping = AtpBlueprintMapping()

    def build(self) -> AtpBlueprintMapping:
        """Build and return AtpBlueprintMapping object.

        Returns:
            AtpBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
