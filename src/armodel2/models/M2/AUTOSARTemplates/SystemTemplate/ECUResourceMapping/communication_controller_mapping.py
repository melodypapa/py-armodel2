"""CommunicationControllerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommunicationControllerMapping(ARObject):
    """AUTOSAR CommunicationControllerMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMMUNICATION-CONTROLLER-MAPPING"


    communication_controller_ref: Optional[ARRef]
    hw_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION-CONTROLLER-REF": ("_POLYMORPHIC", "communication_controller_ref", ["AbstractCanCommunicationController", "CanCommunicationController", "EthernetCommunicationController", "FlexrayCommunicationController", "LinCommunicationController", "LinMaster", "LinSlave", "TtcanCommunicationController", "UserDefinedCommunicationController"]),
        "HW-REF": lambda obj, elem: setattr(obj, "hw_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CommunicationControllerMapping."""
        super().__init__()
        self.communication_controller_ref: Optional[ARRef] = None
        self.hw_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationControllerMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationControllerMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_controller_ref
        if self.communication_controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_controller_ref, "CommunicationController")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_ref
        if self.hw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationControllerMapping":
        """Deserialize XML element to CommunicationControllerMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationControllerMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationControllerMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION-CONTROLLER-REF":
                setattr(obj, "communication_controller_ref", ARRef.deserialize(child))
            elif tag == "HW-REF":
                setattr(obj, "hw_ref", ARRef.deserialize(child))

        return obj



class CommunicationControllerMappingBuilder(BuilderBase):
    """Builder for CommunicationControllerMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationControllerMapping = CommunicationControllerMapping()


    def with_communication_controller(self, value: Optional[CommunicationController]) -> "CommunicationControllerMappingBuilder":
        """Set communication_controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'communication_controller' is required and cannot be None")
        self._obj.communication_controller = value
        return self

    def with_hw(self, value: Optional[HwElement]) -> "CommunicationControllerMappingBuilder":
        """Set hw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'hw' is required and cannot be None")
        self._obj.hw = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "communicationController",
        "hw",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CommunicationControllerMapping:
        """Build and return the CommunicationControllerMapping instance with validation."""
        self._validate_instance()
        return self._obj