"""DiagnosticComControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-COM-CONTROL-CLASS"


    all_channel_refs: list[ARRef]
    all_physical_refs: list[Any]
    specific_channels: list[DiagnosticComControl]
    sub_nodes: list[DiagnosticComControl]
    _DESERIALIZE_DISPATCH = {
        "ALL-CHANNELSES": ("_POLYMORPHIC_LIST", "all_channel_refs", ["AbstractCanCluster", "EthernetCluster", "FlexrayCluster", "LinCluster", "UserDefinedCluster"]),
        "ALL-PHYSICALS": lambda obj, elem: obj.all_physical_refs.append(ARRef.deserialize(elem)),
        "SPECIFIC-CHANNELS": lambda obj, elem: obj.specific_channels.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticComControl")),
        "SUB-NODES": lambda obj, elem: obj.sub_nodes.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticComControl")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channel_refs: list[ARRef] = []
        self.all_physical_refs: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_channel_refs (list to container "ALL-CHANNELS-REFS")
        if self.all_channel_refs:
            wrapper = ET.Element("ALL-CHANNELS-REFS")
            for item in self.all_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationCluster")
                if serialized is not None:
                    child_elem = ET.Element("ALL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize all_physical_refs (list to container "ALL-PHYSICAL-REFS")
        if self.all_physical_refs:
            wrapper = ET.Element("ALL-PHYSICAL-REFS")
            for item in self.all_physical_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ALL-PHYSICAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize specific_channels (list to container "SPECIFIC-CHANNELS")
        if self.specific_channels:
            wrapper = ET.Element("SPECIFIC-CHANNELS")
            for item in self.specific_channels:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_nodes (list to container "SUB-NODES")
        if self.sub_nodes:
            wrapper = ET.Element("SUB-NODES")
            for item in self.sub_nodes:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlClass":
        """Deserialize XML element to DiagnosticComControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControlClass, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ALL-CHANNELSES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-CLUSTER":
                        obj.all_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractCanCluster"))
                    elif concrete_tag == "ETHERNET-CLUSTER":
                        obj.all_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetCluster"))
                    elif concrete_tag == "FLEXRAY-CLUSTER":
                        obj.all_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayCluster"))
                    elif concrete_tag == "LIN-CLUSTER":
                        obj.all_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinCluster"))
                    elif concrete_tag == "USER-DEFINED-CLUSTER":
                        obj.all_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "UserDefinedCluster"))
            elif tag == "ALL-PHYSICALS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.all_physical_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (EthernetPhysical)"))
            elif tag == "SPECIFIC-CHANNELS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.specific_channels.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticComControl"))
            elif tag == "SUB-NODES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sub_nodes.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticComControl"))

        return obj



class DiagnosticComControlClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticComControlClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()


    def with_all_channelses(self, items: list[CommunicationCluster]) -> "DiagnosticComControlClassBuilder":
        """Set all_channelses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.all_channelses = list(items) if items else []
        return self

    def with_all_physicals(self, items: list[any (EthernetPhysical)]) -> "DiagnosticComControlClassBuilder":
        """Set all_physicals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.all_physicals = list(items) if items else []
        return self

    def with_specific_channels(self, items: list[DiagnosticComControl]) -> "DiagnosticComControlClassBuilder":
        """Set specific_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.specific_channels = list(items) if items else []
        return self

    def with_sub_nodes(self, items: list[DiagnosticComControl]) -> "DiagnosticComControlClassBuilder":
        """Set sub_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes = list(items) if items else []
        return self


    def add_all_channels(self, item: CommunicationCluster) -> "DiagnosticComControlClassBuilder":
        """Add a single item to all_channelses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.all_channelses.append(item)
        return self

    def clear_all_channelses(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from all_channelses list.

        Returns:
            self for method chaining
        """
        self._obj.all_channelses = []
        return self

    def add_all_physical(self, item: any (EthernetPhysical)) -> "DiagnosticComControlClassBuilder":
        """Add a single item to all_physicals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.all_physicals.append(item)
        return self

    def clear_all_physicals(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from all_physicals list.

        Returns:
            self for method chaining
        """
        self._obj.all_physicals = []
        return self

    def add_specific_channel(self, item: DiagnosticComControl) -> "DiagnosticComControlClassBuilder":
        """Add a single item to specific_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.specific_channels.append(item)
        return self

    def clear_specific_channels(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from specific_channels list.

        Returns:
            self for method chaining
        """
        self._obj.specific_channels = []
        return self

    def add_sub_node(self, item: DiagnosticComControl) -> "DiagnosticComControlClassBuilder":
        """Add a single item to sub_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes.append(item)
        return self

    def clear_sub_nodes(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from sub_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes = []
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


    def build(self) -> DiagnosticComControlClass:
        """Build and return the DiagnosticComControlClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj