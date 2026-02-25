"""LinMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config import (
    LinSlaveConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class LinMaster(ARObject):
    """AUTOSAR LinMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lin_slaves: list[LinSlaveConfig]
    time_base: Optional[TimeValue]
    time_base_jitter: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize LinMaster."""
        super().__init__()
        self.lin_slaves: list[LinSlaveConfig] = []
        self.time_base: Optional[TimeValue] = None
        self.time_base_jitter: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize LinMaster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinMaster, self).serialize()

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

        # Serialize lin_slaves (list)
        for item in self.lin_slaves:
            serialized = SerializationHelper.serialize_item(item, "LinSlaveConfig")
            if serialized is not None:
                wrapped = ET.Element("LIN-SLAF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_base
        if self.time_base is not None:
            serialized = SerializationHelper.serialize_item(self.time_base, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("TIME-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_base_jitter
        if self.time_base_jitter is not None:
            serialized = SerializationHelper.serialize_item(self.time_base_jitter, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("TIME-BASE-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "LinMaster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinMaster":
        """Deserialize XML element to LinMaster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinMaster object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "LinMaster")
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
        obj = super(LinMaster, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse lin_slaves (list)
        obj.lin_slaves = []
        for child in SerializationHelper.find_all_child_elements(inner_elem, "LIN-SLAF"):
            lin_slaves_value = SerializationHelper.deserialize_by_tag(child, "LinSlaveConfig")
            obj.lin_slaves.append(lin_slaves_value)

        # Parse time_base
        child = SerializationHelper.find_child_element(inner_elem, "TIME-BASE")
        if child is not None:
            time_base_value = child.text
            obj.time_base = time_base_value

        # Parse time_base_jitter
        child = SerializationHelper.find_child_element(inner_elem, "TIME-BASE-JITTER")
        if child is not None:
            time_base_jitter_value = child.text
            obj.time_base_jitter = time_base_jitter_value

        return obj



class LinMasterBuilder(BuilderBase):
    """Builder for LinMaster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinMaster = LinMaster()


    def with_lin_slaves(self, items: list[LinSlaveConfig]) -> "LinMasterBuilder":
        """Set lin_slaves list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_slaves = list(items) if items else []
        return self

    def with_time_base(self, value: Optional[TimeValue]) -> "LinMasterBuilder":
        """Set time_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_base = value
        return self

    def with_time_base_jitter(self, value: Optional[TimeValue]) -> "LinMasterBuilder":
        """Set time_base_jitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_base_jitter = value
        return self


    def add_lin_slaf(self, item: LinSlaveConfig) -> "LinMasterBuilder":
        """Add a single item to lin_slaves list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_slaves.append(item)
        return self

    def clear_lin_slaves(self) -> "LinMasterBuilder":
        """Clear all items from lin_slaves list.

        Returns:
            self for method chaining
        """
        self._obj.lin_slaves = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> LinMaster:
        """Build and return the LinMaster instance with validation."""
        self._validate_instance()
        pass
        return self._obj