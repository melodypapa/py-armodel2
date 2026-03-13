"""McDataAccessDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
        VariableAccess,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class McDataAccessDetails(ARObject):
    """AUTOSAR McDataAccessDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-DATA-ACCESS-DETAILS"


    rte_event_irefs: list[RTEEvent]
    variable_acces_irefs: list[VariableAccess]
    _DESERIALIZE_DISPATCH = {
        "RTE-EVENTS-IREF": ("_POLYMORPHIC_LIST", "rte_event_irefs", ["AsynchronousServerCallReturnsEvent", "BackgroundEvent", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "ExternalTriggerOccurredEvent", "InitEvent", "InternalTriggerOccurredEvent", "ModeSwitchedAckEvent", "OperationInvokedEvent", "OsTaskExecutionEvent", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "TimingEvent", "TransformerHardErrorEvent"]),
        "VARIABLE-ACCESSS-IREF": lambda obj, elem: obj.variable_acces_irefs.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
    }


    def __init__(self) -> None:
        """Initialize McDataAccessDetails."""
        super().__init__()
        self.rte_event_irefs: list[RTEEvent] = []
        self.variable_acces_irefs: list[VariableAccess] = []

    def serialize(self) -> ET.Element:
        """Serialize McDataAccessDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McDataAccessDetails, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rte_event_irefs (list of instance references with wrapper "RTE-EVENTS-IREF")
        if self.rte_event_irefs:
            serialized = SerializationHelper.serialize_item(self.rte_event_irefs, "RTEEvent")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("RTE-EVENTS-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize variable_acces_irefs (list of instance references with wrapper "VARIABLE-ACCESSS-IREF")
        if self.variable_acces_irefs:
            serialized = SerializationHelper.serialize_item(self.variable_acces_irefs, "VariableAccess")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("VARIABLE-ACCESSS-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataAccessDetails":
        """Deserialize XML element to McDataAccessDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataAccessDetails object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McDataAccessDetails, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RTE-EVENT-IREFS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "BackgroundEvent"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "DataWriteCompletedEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "INIT-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchedAckEvent"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "OsTaskExecutionEvent"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeSwitchEvent"))
                    elif concrete_tag == "TIMING-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        obj.rte_event_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "TransformerHardErrorEvent"))
            elif tag == "VARIABLE-ACCESS-IREFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.variable_acces_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))

        return obj



class McDataAccessDetailsBuilder(BuilderBase):
    """Builder for McDataAccessDetails with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McDataAccessDetails = McDataAccessDetails()


    def with_rte_events(self, items: list[RTEEvent]) -> "McDataAccessDetailsBuilder":
        """Set rte_events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_events = list(items) if items else []
        return self

    def with_variable_accesses(self, items: list[VariableAccess]) -> "McDataAccessDetailsBuilder":
        """Set variable_accesses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses = list(items) if items else []
        return self


    def add_rte_event(self, item: RTEEvent) -> "McDataAccessDetailsBuilder":
        """Add a single item to rte_events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_events.append(item)
        return self

    def clear_rte_events(self) -> "McDataAccessDetailsBuilder":
        """Clear all items from rte_events list.

        Returns:
            self for method chaining
        """
        self._obj.rte_events = []
        return self

    def add_variable_access(self, item: VariableAccess) -> "McDataAccessDetailsBuilder":
        """Add a single item to variable_accesses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses.append(item)
        return self

    def clear_variable_accesses(self) -> "McDataAccessDetailsBuilder":
        """Clear all items from variable_accesses list.

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "rteEvent",
        "variableAccess",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> McDataAccessDetails:
        """Build and return the McDataAccessDetails instance with validation."""
        self._validate_instance()
        return self._obj