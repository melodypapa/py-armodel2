"""J1939ControllerApplicationToJ1939NmNodeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """AUTOSAR J1939ControllerApplicationToJ1939NmNodeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-CONTROLLER-APPLICATION-TO-J1939-NM-NODE-MAPPING"


    j1939_controller_ref: Optional[Any]
    j1939_nm_node_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "J1939-CONTROLLER-REF": lambda obj, elem: setattr(obj, "j1939_controller_ref", ARRef.deserialize(elem)),
        "J1939-NM-NODE-REF": lambda obj, elem: setattr(obj, "j1939_nm_node_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize J1939ControllerApplicationToJ1939NmNodeMapping."""
        super().__init__()
        self.j1939_controller_ref: Optional[Any] = None
        self.j1939_nm_node_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939ControllerApplicationToJ1939NmNodeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939ControllerApplicationToJ1939NmNodeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize j1939_controller_ref
        if self.j1939_controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.j1939_controller_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("J1939-CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize j1939_nm_node_ref
        if self.j1939_nm_node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.j1939_nm_node_ref, "J1939NmNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("J1939-NM-NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939ControllerApplicationToJ1939NmNodeMapping":
        """Deserialize XML element to J1939ControllerApplicationToJ1939NmNodeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939ControllerApplicationToJ1939NmNodeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939ControllerApplicationToJ1939NmNodeMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "J1939-CONTROLLER-REF":
                setattr(obj, "j1939_controller_ref", ARRef.deserialize(child))
            elif tag == "J1939-NM-NODE-REF":
                setattr(obj, "j1939_nm_node_ref", ARRef.deserialize(child))

        return obj



class J1939ControllerApplicationToJ1939NmNodeMappingBuilder(BuilderBase):
    """Builder for J1939ControllerApplicationToJ1939NmNodeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939ControllerApplicationToJ1939NmNodeMapping = J1939ControllerApplicationToJ1939NmNodeMapping()


    def with_j1939_controller(self, value: Optional[Any]) -> "J1939ControllerApplicationToJ1939NmNodeMappingBuilder":
        """Set j1939_controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'j1939_controller' is required and cannot be None")
        self._obj.j1939_controller = value
        return self

    def with_j1939_nm_node(self, value: Optional[J1939NmNode]) -> "J1939ControllerApplicationToJ1939NmNodeMappingBuilder":
        """Set j1939_nm_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'j1939_nm_node' is required and cannot be None")
        self._obj.j1939_nm_node = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "j1939Controller",
        "j1939NmNode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> J1939ControllerApplicationToJ1939NmNodeMapping:
        """Build and return the J1939ControllerApplicationToJ1939NmNodeMapping instance with validation."""
        self._validate_instance()
        return self._obj