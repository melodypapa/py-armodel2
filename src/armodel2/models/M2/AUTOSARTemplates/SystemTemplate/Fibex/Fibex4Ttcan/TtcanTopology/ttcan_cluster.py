"""TtcanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_variant()

class TtcanCluster(ARObject):
    """AUTOSAR TtcanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TTCAN-CLUSTER"


    basic_cycle_length: Optional[Integer]
    ntu: Optional[TimeValue]
    operation_mode: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "BASIC-CYCLE-LENGTH": lambda obj, elem: setattr(obj, "basic_cycle_length", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NTU": lambda obj, elem: setattr(obj, "ntu", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "OPERATION-MODE": lambda obj, elem: setattr(obj, "operation_mode", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize TtcanCluster."""
        super().__init__()
        self.basic_cycle_length: Optional[Integer] = None
        self.ntu: Optional[TimeValue] = None
        self.operation_mode: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TtcanCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TtcanCluster, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize basic_cycle_length
        if self.basic_cycle_length is not None:
            serialized = SerializationHelper.serialize_item(self.basic_cycle_length, "Integer")
            if serialized is not None:
                wrapped = ET.Element("BASIC-CYCLE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize ntu
        if self.ntu is not None:
            serialized = SerializationHelper.serialize_item(self.ntu, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("NTU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize operation_mode
        if self.operation_mode is not None:
            serialized = SerializationHelper.serialize_item(self.operation_mode, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("OPERATION-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TtcanCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCluster":
        """Deserialize XML element to TtcanCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCluster object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TtcanCluster")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(TtcanCluster, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse basic_cycle_length
        child = SerializationHelper.find_child_element(inner_elem, "BASIC-CYCLE-LENGTH")
        if child is not None:
            basic_cycle_length_value = child.text
            obj.basic_cycle_length = basic_cycle_length_value

        # Parse ntu
        child = SerializationHelper.find_child_element(inner_elem, "NTU")
        if child is not None:
            ntu_value = child.text
            obj.ntu = ntu_value

        # Parse operation_mode
        child = SerializationHelper.find_child_element(inner_elem, "OPERATION-MODE")
        if child is not None:
            operation_mode_value = child.text
            obj.operation_mode = operation_mode_value

        return obj



class TtcanClusterBuilder(BuilderBase):
    """Builder for TtcanCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TtcanCluster = TtcanCluster()


    def with_basic_cycle_length(self, value: Optional[Integer]) -> "TtcanClusterBuilder":
        """Set basic_cycle_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.basic_cycle_length = value
        return self

    def with_ntu(self, value: Optional[TimeValue]) -> "TtcanClusterBuilder":
        """Set ntu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ntu = value
        return self

    def with_operation_mode(self, value: Optional[Boolean]) -> "TtcanClusterBuilder":
        """Set operation_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.operation_mode = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "basicCycleLength",
        "ntu",
        "operationMode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TtcanCluster:
        """Build and return the TtcanCluster instance with validation."""
        self._validate_instance()
        return self._obj