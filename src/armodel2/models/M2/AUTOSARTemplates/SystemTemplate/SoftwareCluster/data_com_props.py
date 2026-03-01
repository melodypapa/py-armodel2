"""DataComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import CpSoftwareClusterCommunicationResourcePropsBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    DataConsistencyPolicyEnum,
    SendIndicationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR DataComProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-COM-PROPS"


    data: Optional[DataConsistencyPolicyEnum]
    send_indication_enum: Optional[SendIndicationEnum]
    _DESERIALIZE_DISPATCH = {
        "DATA": lambda obj, elem: setattr(obj, "data", DataConsistencyPolicyEnum.deserialize(elem)),
        "SEND-INDICATION-ENUM": lambda obj, elem: setattr(obj, "send_indication_enum", SendIndicationEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DataComProps."""
        super().__init__()
        self.data: Optional[DataConsistencyPolicyEnum] = None
        self.send_indication_enum: Optional[SendIndicationEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DataComProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataComProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data
        if self.data is not None:
            serialized = SerializationHelper.serialize_item(self.data, "DataConsistencyPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize send_indication_enum
        if self.send_indication_enum is not None:
            serialized = SerializationHelper.serialize_item(self.send_indication_enum, "SendIndicationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEND-INDICATION-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataComProps":
        """Deserialize XML element to DataComProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataComProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataComProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DATA":
                setattr(obj, "data", DataConsistencyPolicyEnum.deserialize(child))
            elif tag == "SEND-INDICATION-ENUM":
                setattr(obj, "send_indication_enum", SendIndicationEnum.deserialize(child))

        return obj



class DataComPropsBuilder(CpSoftwareClusterCommunicationResourcePropsBuilder):
    """Builder for DataComProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataComProps = DataComProps()


    def with_data(self, value: Optional[DataConsistencyPolicyEnum]) -> "DataComPropsBuilder":
        """Set data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data = value
        return self

    def with_send_indication_enum(self, value: Optional[SendIndicationEnum]) -> "DataComPropsBuilder":
        """Set send_indication_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.send_indication_enum = value
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


    def build(self) -> DataComProps:
        """Build and return the DataComProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj