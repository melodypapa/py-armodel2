"""NvBlockSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 663)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import AtomicSwComponentTypeBuilder
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class NvBlockSwComponentType(AtomicSwComponentType):
    """AUTOSAR NvBlockSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bulk_nv_datas: list[BulkNvDataDescriptor]
    nv_blocks: list[NvBlockDescriptor]
    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_datas: list[BulkNvDataDescriptor] = []
        self.nv_blocks: list[NvBlockDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bulk_nv_datas (list to container "BULK-NV-DATAS")
        if self.bulk_nv_datas:
            wrapper = ET.Element("BULK-NV-DATAS")
            for item in self.bulk_nv_datas:
                serialized = SerializationHelper.serialize_item(item, "BulkNvDataDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_blocks (list to container "NV-BLOCKS")
        if self.nv_blocks:
            wrapper = ET.Element("NV-BLOCKS")
            for item in self.nv_blocks:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockSwComponentType":
        """Deserialize XML element to NvBlockSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockSwComponentType, cls).deserialize(element)

        # Parse bulk_nv_datas (list from container "BULK-NV-DATAS")
        obj.bulk_nv_datas = []
        container = SerializationHelper.find_child_element(element, "BULK-NV-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bulk_nv_datas.append(child_value)

        # Parse nv_blocks (list from container "NV-BLOCKS")
        obj.nv_blocks = []
        container = SerializationHelper.find_child_element(element, "NV-BLOCKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_blocks.append(child_value)

        return obj



class NvBlockSwComponentTypeBuilder(AtomicSwComponentTypeBuilder):
    """Builder for NvBlockSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockSwComponentType = NvBlockSwComponentType()


    def with_bulk_nv_datas(self, items: list[BulkNvDataDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set bulk_nv_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas = list(items) if items else []
        return self

    def with_nv_blocks(self, items: list[NvBlockDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set nv_blocks list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks = list(items) if items else []
        return self


    def add_bulk_nv_data(self, item: BulkNvDataDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to bulk_nv_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas.append(item)
        return self

    def clear_bulk_nv_datas(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from bulk_nv_datas list.

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas = []
        return self

    def add_nv_block(self, item: NvBlockDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to nv_blocks list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks.append(item)
        return self

    def clear_nv_blocks(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from nv_blocks list.

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks = []
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


    def build(self) -> NvBlockSwComponentType:
        """Build and return the NvBlockSwComponentType instance with validation."""
        self._validate_instance()
        pass
        return self._obj