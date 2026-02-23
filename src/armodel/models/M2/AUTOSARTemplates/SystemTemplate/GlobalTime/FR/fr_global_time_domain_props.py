"""FrGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import AbstractGlobalTimeDomainPropsBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR FrGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ofs_data_id_list: PositiveInteger
    sync_data_id_list: PositiveInteger
    def __init__(self) -> None:
        """Initialize FrGlobalTimeDomainProps."""
        super().__init__()
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize FrGlobalTimeDomainProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FrGlobalTimeDomainProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ofs_data_id_list
        if self.ofs_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.ofs_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFS-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_data_id_list
        if self.sync_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.sync_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrGlobalTimeDomainProps":
        """Deserialize XML element to FrGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FrGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FrGlobalTimeDomainProps, cls).deserialize(element)

        # Parse ofs_data_id_list
        child = SerializationHelper.find_child_element(element, "OFS-DATA-ID-LIST")
        if child is not None:
            ofs_data_id_list_value = child.text
            obj.ofs_data_id_list = ofs_data_id_list_value

        # Parse sync_data_id_list
        child = SerializationHelper.find_child_element(element, "SYNC-DATA-ID-LIST")
        if child is not None:
            sync_data_id_list_value = child.text
            obj.sync_data_id_list = sync_data_id_list_value

        return obj



class FrGlobalTimeDomainPropsBuilder(AbstractGlobalTimeDomainPropsBuilder):
    """Builder for FrGlobalTimeDomainProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FrGlobalTimeDomainProps = FrGlobalTimeDomainProps()


    def with_ofs_data_id_list(self, value: PositiveInteger) -> "FrGlobalTimeDomainPropsBuilder":
        """Set ofs_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ofs_data_id_list = value
        return self

    def with_sync_data_id_list(self, value: PositiveInteger) -> "FrGlobalTimeDomainPropsBuilder":
        """Set sync_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_data_id_list = value
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


    def build(self) -> FrGlobalTimeDomainProps:
        """Build and return the FrGlobalTimeDomainProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj