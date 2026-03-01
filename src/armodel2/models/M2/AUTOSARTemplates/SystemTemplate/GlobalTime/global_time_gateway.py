"""GlobalTimeGateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 861)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeGateway(Identifiable):
    """AUTOSAR GlobalTimeGateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-GATEWAY"


    host_ref: Optional[ARRef]
    master_ref: Optional[ARRef]
    slave_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HOST-REF": lambda obj, elem: setattr(obj, "host_ref", ARRef.deserialize(elem)),
        "MASTER-REF": ("_POLYMORPHIC", "master_ref", ["GlobalTimeCanMaster", "GlobalTimeEthMaster", "GlobalTimeFrMaster", "UserDefinedGlobalTimeMaster"]),
        "SLAVE-REF": ("_POLYMORPHIC", "slave_ref", ["GlobalTimeCanSlave", "GlobalTimeEthSlave", "GlobalTimeFrSlave", "UserDefinedGlobalTimeSlave"]),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeGateway."""
        super().__init__()
        self.host_ref: Optional[ARRef] = None
        self.master_ref: Optional[ARRef] = None
        self.slave_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeGateway to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeGateway, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize host_ref
        if self.host_ref is not None:
            serialized = SerializationHelper.serialize_item(self.host_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize master_ref
        if self.master_ref is not None:
            serialized = SerializationHelper.serialize_item(self.master_ref, "GlobalTimeMaster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave_ref
        if self.slave_ref is not None:
            serialized = SerializationHelper.serialize_item(self.slave_ref, "GlobalTimeSlave")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeGateway":
        """Deserialize XML element to GlobalTimeGateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeGateway object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeGateway, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "HOST-REF":
                setattr(obj, "host_ref", ARRef.deserialize(child))
            elif tag == "MASTER-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "GLOBAL-TIME-CAN-MASTER":
                        setattr(obj, "master_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeCanMaster"))
                    elif concrete_tag == "GLOBAL-TIME-ETH-MASTER":
                        setattr(obj, "master_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeEthMaster"))
                    elif concrete_tag == "GLOBAL-TIME-FR-MASTER":
                        setattr(obj, "master_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeFrMaster"))
                    elif concrete_tag == "USER-DEFINED-GLOBAL-TIME-MASTER":
                        setattr(obj, "master_ref", SerializationHelper.deserialize_by_tag(child[0], "UserDefinedGlobalTimeMaster"))
            elif tag == "SLAVE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "GLOBAL-TIME-CAN-SLAVE":
                        setattr(obj, "slave_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeCanSlave"))
                    elif concrete_tag == "GLOBAL-TIME-ETH-SLAVE":
                        setattr(obj, "slave_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeEthSlave"))
                    elif concrete_tag == "GLOBAL-TIME-FR-SLAVE":
                        setattr(obj, "slave_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeFrSlave"))
                    elif concrete_tag == "USER-DEFINED-GLOBAL-TIME-SLAVE":
                        setattr(obj, "slave_ref", SerializationHelper.deserialize_by_tag(child[0], "UserDefinedGlobalTimeSlave"))

        return obj



class GlobalTimeGatewayBuilder(IdentifiableBuilder):
    """Builder for GlobalTimeGateway with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeGateway = GlobalTimeGateway()


    def with_host(self, value: Optional[EcuInstance]) -> "GlobalTimeGatewayBuilder":
        """Set host attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.host = value
        return self

    def with_master(self, value: Optional[GlobalTimeMaster]) -> "GlobalTimeGatewayBuilder":
        """Set master attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.master = value
        return self

    def with_slave(self, value: Optional[GlobalTimeSlave]) -> "GlobalTimeGatewayBuilder":
        """Set slave attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slave = value
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


    def build(self) -> GlobalTimeGateway:
        """Build and return the GlobalTimeGateway instance with validation."""
        self._validate_instance()
        pass
        return self._obj