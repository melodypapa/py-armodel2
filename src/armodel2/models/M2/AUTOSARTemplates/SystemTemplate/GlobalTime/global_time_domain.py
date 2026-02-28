"""GlobalTimeDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 858)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 225)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
    GlobalTimeGateway,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
    NetworkSegmentIdentification,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeDomain(FibexElement):
    """AUTOSAR GlobalTimeDomain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-DOMAIN"


    debounce_time: Optional[TimeValue]
    domain_id: Optional[PositiveInteger]
    gatewaies: list[GlobalTimeGateway]
    global_time: Optional[AbstractGlobalTimeDomainProps]
    global_time_master: Optional[GlobalTimeMaster]
    global_time_sub_refs: list[ARRef]
    network: Optional[NetworkSegmentIdentification]
    offset_time_ref: Optional[ARRef]
    pdu_triggering_ref: Optional[ARRef]
    slaves: list[GlobalTimeSlave]
    sync_loss: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "DEBOUNCE-TIME": lambda obj, elem: setattr(obj, "debounce_time", elem.text),
        "DOMAIN-ID": lambda obj, elem: setattr(obj, "domain_id", elem.text),
        "GATEWAIES": lambda obj, elem: obj.gatewaies.append(GlobalTimeGateway.deserialize(elem)),
        "GLOBAL-TIME": lambda obj, elem: setattr(obj, "global_time", AbstractGlobalTimeDomainProps.deserialize(elem)),
        "GLOBAL-TIME-MASTER": lambda obj, elem: setattr(obj, "global_time_master", GlobalTimeMaster.deserialize(elem)),
        "GLOBAL-TIME-SUBS": lambda obj, elem: obj.global_time_sub_refs.append(ARRef.deserialize(elem)),
        "NETWORK": lambda obj, elem: setattr(obj, "network", NetworkSegmentIdentification.deserialize(elem)),
        "OFFSET-TIME-REF": lambda obj, elem: setattr(obj, "offset_time_ref", ARRef.deserialize(elem)),
        "PDU-TRIGGERING-REF": lambda obj, elem: setattr(obj, "pdu_triggering_ref", ARRef.deserialize(elem)),
        "SLAVES": lambda obj, elem: obj.slaves.append(GlobalTimeSlave.deserialize(elem)),
        "SYNC-LOSS": lambda obj, elem: setattr(obj, "sync_loss", elem.text),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeDomain."""
        super().__init__()
        self.debounce_time: Optional[TimeValue] = None
        self.domain_id: Optional[PositiveInteger] = None
        self.gatewaies: list[GlobalTimeGateway] = []
        self.global_time: Optional[AbstractGlobalTimeDomainProps] = None
        self.global_time_master: Optional[GlobalTimeMaster] = None
        self.global_time_sub_refs: list[ARRef] = []
        self.network: Optional[NetworkSegmentIdentification] = None
        self.offset_time_ref: Optional[ARRef] = None
        self.pdu_triggering_ref: Optional[ARRef] = None
        self.slaves: list[GlobalTimeSlave] = []
        self.sync_loss: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeDomain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeDomain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize debounce_time
        if self.debounce_time is not None:
            serialized = SerializationHelper.serialize_item(self.debounce_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEBOUNCE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize domain_id
        if self.domain_id is not None:
            serialized = SerializationHelper.serialize_item(self.domain_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize gatewaies (list to container "GATEWAIES")
        if self.gatewaies:
            wrapper = ET.Element("GATEWAIES")
            for item in self.gatewaies:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeGateway")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_time
        if self.global_time is not None:
            serialized = SerializationHelper.serialize_item(self.global_time, "AbstractGlobalTimeDomainProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_master
        if self.global_time_master is not None:
            serialized = SerializationHelper.serialize_item(self.global_time_master, "GlobalTimeMaster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME-MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_sub_refs (list to container "GLOBAL-TIME-SUB-REFS")
        if self.global_time_sub_refs:
            wrapper = ET.Element("GLOBAL-TIME-SUB-REFS")
            for item in self.global_time_sub_refs:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeDomain")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-TIME-SUB-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "NetworkSegmentIdentification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset_time_ref
        if self.offset_time_ref is not None:
            serialized = SerializationHelper.serialize_item(self.offset_time_ref, "GlobalTimeDomain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-TIME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_triggering_ref
        if self.pdu_triggering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-TRIGGERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slaves (list to container "SLAVES")
        if self.slaves:
            wrapper = ET.Element("SLAVES")
            for item in self.slaves:
                serialized = SerializationHelper.serialize_item(item, "GlobalTimeSlave")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sync_loss
        if self.sync_loss is not None:
            serialized = SerializationHelper.serialize_item(self.sync_loss, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-LOSS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeDomain":
        """Deserialize XML element to GlobalTimeDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeDomain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeDomain, cls).deserialize(element)

        # Parse debounce_time
        child = SerializationHelper.find_child_element(element, "DEBOUNCE-TIME")
        if child is not None:
            debounce_time_value = child.text
            obj.debounce_time = debounce_time_value

        # Parse domain_id
        child = SerializationHelper.find_child_element(element, "DOMAIN-ID")
        if child is not None:
            domain_id_value = child.text
            obj.domain_id = domain_id_value

        # Parse gatewaies (list from container "GATEWAIES")
        obj.gatewaies = []
        container = SerializationHelper.find_child_element(element, "GATEWAIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.gatewaies.append(child_value)

        # Parse global_time
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME")
        if child is not None:
            global_time_value = SerializationHelper.deserialize_by_tag(child, "AbstractGlobalTimeDomainProps")
            obj.global_time = global_time_value

        # Parse global_time_master
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME-MASTER")
        if child is not None:
            global_time_master_value = SerializationHelper.deserialize_by_tag(child, "GlobalTimeMaster")
            obj.global_time_master = global_time_master_value

        # Parse global_time_sub_refs (list from container "GLOBAL-TIME-SUB-REFS")
        obj.global_time_sub_refs = []
        container = SerializationHelper.find_child_element(element, "GLOBAL-TIME-SUB-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_time_sub_refs.append(child_value)

        # Parse network
        child = SerializationHelper.find_child_element(element, "NETWORK")
        if child is not None:
            network_value = SerializationHelper.deserialize_by_tag(child, "NetworkSegmentIdentification")
            obj.network = network_value

        # Parse offset_time_ref
        child = SerializationHelper.find_child_element(element, "OFFSET-TIME-REF")
        if child is not None:
            offset_time_ref_value = ARRef.deserialize(child)
            obj.offset_time_ref = offset_time_ref_value

        # Parse pdu_triggering_ref
        child = SerializationHelper.find_child_element(element, "PDU-TRIGGERING-REF")
        if child is not None:
            pdu_triggering_ref_value = ARRef.deserialize(child)
            obj.pdu_triggering_ref = pdu_triggering_ref_value

        # Parse slaves (list from container "SLAVES")
        obj.slaves = []
        container = SerializationHelper.find_child_element(element, "SLAVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.slaves.append(child_value)

        # Parse sync_loss
        child = SerializationHelper.find_child_element(element, "SYNC-LOSS")
        if child is not None:
            sync_loss_value = child.text
            obj.sync_loss = sync_loss_value

        return obj



class GlobalTimeDomainBuilder(FibexElementBuilder):
    """Builder for GlobalTimeDomain with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeDomain = GlobalTimeDomain()


    def with_debounce_time(self, value: Optional[TimeValue]) -> "GlobalTimeDomainBuilder":
        """Set debounce_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.debounce_time = value
        return self

    def with_domain_id(self, value: Optional[PositiveInteger]) -> "GlobalTimeDomainBuilder":
        """Set domain_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.domain_id = value
        return self

    def with_gatewaies(self, items: list[GlobalTimeGateway]) -> "GlobalTimeDomainBuilder":
        """Set gatewaies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.gatewaies = list(items) if items else []
        return self

    def with_global_time(self, value: Optional[AbstractGlobalTimeDomainProps]) -> "GlobalTimeDomainBuilder":
        """Set global_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_time = value
        return self

    def with_global_time_master(self, value: Optional[GlobalTimeMaster]) -> "GlobalTimeDomainBuilder":
        """Set global_time_master attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_time_master = value
        return self

    def with_global_time_subs(self, items: list[GlobalTimeDomain]) -> "GlobalTimeDomainBuilder":
        """Set global_time_subs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.global_time_subs = list(items) if items else []
        return self

    def with_network(self, value: Optional[NetworkSegmentIdentification]) -> "GlobalTimeDomainBuilder":
        """Set network attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network = value
        return self

    def with_offset_time(self, value: Optional[GlobalTimeDomain]) -> "GlobalTimeDomainBuilder":
        """Set offset_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset_time = value
        return self

    def with_pdu_triggering(self, value: Optional[PduTriggering]) -> "GlobalTimeDomainBuilder":
        """Set pdu_triggering attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_triggering = value
        return self

    def with_slaves(self, items: list[GlobalTimeSlave]) -> "GlobalTimeDomainBuilder":
        """Set slaves list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.slaves = list(items) if items else []
        return self

    def with_sync_loss(self, value: Optional[TimeValue]) -> "GlobalTimeDomainBuilder":
        """Set sync_loss attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_loss = value
        return self


    def add_gateway(self, item: GlobalTimeGateway) -> "GlobalTimeDomainBuilder":
        """Add a single item to gatewaies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.gatewaies.append(item)
        return self

    def clear_gatewaies(self) -> "GlobalTimeDomainBuilder":
        """Clear all items from gatewaies list.

        Returns:
            self for method chaining
        """
        self._obj.gatewaies = []
        return self

    def add_global_time_sub(self, item: GlobalTimeDomain) -> "GlobalTimeDomainBuilder":
        """Add a single item to global_time_subs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.global_time_subs.append(item)
        return self

    def clear_global_time_subs(self) -> "GlobalTimeDomainBuilder":
        """Clear all items from global_time_subs list.

        Returns:
            self for method chaining
        """
        self._obj.global_time_subs = []
        return self

    def add_slaf(self, item: GlobalTimeSlave) -> "GlobalTimeDomainBuilder":
        """Add a single item to slaves list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.slaves.append(item)
        return self

    def clear_slaves(self) -> "GlobalTimeDomainBuilder":
        """Clear all items from slaves list.

        Returns:
            self for method chaining
        """
        self._obj.slaves = []
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


    def build(self) -> GlobalTimeDomain:
        """Build and return the GlobalTimeDomain instance with validation."""
        self._validate_instance()
        pass
        return self._obj