"""SwitchFlowMeteringEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    FlowMeteringColorModeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwitchFlowMeteringEntry(Identifiable):
    """AUTOSAR SwitchFlowMeteringEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    color_mode: Optional[FlowMeteringColorModeEnum]
    committed_burst: Optional[PositiveInteger]
    committed: Optional[PositiveInteger]
    coupling_flag: Optional[Boolean]
    excess_burst: Optional[PositiveInteger]
    excess: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchFlowMeteringEntry."""
        super().__init__()
        self.color_mode: Optional[FlowMeteringColorModeEnum] = None
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.coupling_flag: Optional[Boolean] = None
        self.excess_burst: Optional[PositiveInteger] = None
        self.excess: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchFlowMeteringEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchFlowMeteringEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize color_mode
        if self.color_mode is not None:
            serialized = SerializationHelper.serialize_item(self.color_mode, "FlowMeteringColorModeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLOR-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize committed_burst
        if self.committed_burst is not None:
            serialized = SerializationHelper.serialize_item(self.committed_burst, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMITTED-BURST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize committed
        if self.committed is not None:
            serialized = SerializationHelper.serialize_item(self.committed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMITTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coupling_flag
        if self.coupling_flag is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_flag, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-FLAG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize excess_burst
        if self.excess_burst is not None:
            serialized = SerializationHelper.serialize_item(self.excess_burst, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCESS-BURST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize excess
        if self.excess is not None:
            serialized = SerializationHelper.serialize_item(self.excess, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchFlowMeteringEntry":
        """Deserialize XML element to SwitchFlowMeteringEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchFlowMeteringEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchFlowMeteringEntry, cls).deserialize(element)

        # Parse color_mode
        child = SerializationHelper.find_child_element(element, "COLOR-MODE")
        if child is not None:
            color_mode_value = FlowMeteringColorModeEnum.deserialize(child)
            obj.color_mode = color_mode_value

        # Parse committed_burst
        child = SerializationHelper.find_child_element(element, "COMMITTED-BURST")
        if child is not None:
            committed_burst_value = child.text
            obj.committed_burst = committed_burst_value

        # Parse committed
        child = SerializationHelper.find_child_element(element, "COMMITTED")
        if child is not None:
            committed_value = child.text
            obj.committed = committed_value

        # Parse coupling_flag
        child = SerializationHelper.find_child_element(element, "COUPLING-FLAG")
        if child is not None:
            coupling_flag_value = child.text
            obj.coupling_flag = coupling_flag_value

        # Parse excess_burst
        child = SerializationHelper.find_child_element(element, "EXCESS-BURST")
        if child is not None:
            excess_burst_value = child.text
            obj.excess_burst = excess_burst_value

        # Parse excess
        child = SerializationHelper.find_child_element(element, "EXCESS")
        if child is not None:
            excess_value = child.text
            obj.excess = excess_value

        return obj



class SwitchFlowMeteringEntryBuilder(IdentifiableBuilder):
    """Builder for SwitchFlowMeteringEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchFlowMeteringEntry = SwitchFlowMeteringEntry()


    def with_color_mode(self, value: Optional[FlowMeteringColorModeEnum]) -> "SwitchFlowMeteringEntryBuilder":
        """Set color_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.color_mode = value
        return self

    def with_committed_burst(self, value: Optional[PositiveInteger]) -> "SwitchFlowMeteringEntryBuilder":
        """Set committed_burst attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.committed_burst = value
        return self

    def with_committed(self, value: Optional[PositiveInteger]) -> "SwitchFlowMeteringEntryBuilder":
        """Set committed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.committed = value
        return self

    def with_coupling_flag(self, value: Optional[Boolean]) -> "SwitchFlowMeteringEntryBuilder":
        """Set coupling_flag attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coupling_flag = value
        return self

    def with_excess_burst(self, value: Optional[PositiveInteger]) -> "SwitchFlowMeteringEntryBuilder":
        """Set excess_burst attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.excess_burst = value
        return self

    def with_excess(self, value: Optional[PositiveInteger]) -> "SwitchFlowMeteringEntryBuilder":
        """Set excess attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.excess = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> SwitchFlowMeteringEntry:
        """Build and return the SwitchFlowMeteringEntry instance with validation."""
        self._validate_instance()
        pass
        return self._obj