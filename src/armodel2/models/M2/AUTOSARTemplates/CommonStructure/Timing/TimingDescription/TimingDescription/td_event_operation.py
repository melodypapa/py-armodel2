"""TDEventOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import TDEventVfbPortBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventOperationTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventOperation(TDEventVfbPort):
    """AUTOSAR TDEventOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-OPERATION"


    operation_ref: Optional[ARRef]
    td_event: Optional[TDEventOperationTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "OPERATION-REF": lambda obj, elem: setattr(obj, "operation_ref", ARRef.deserialize(elem)),
        "TD-EVENT": lambda obj, elem: setattr(obj, "td_event", TDEventOperationTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDEventOperation."""
        super().__init__()
        self.operation_ref: Optional[ARRef] = None
        self.td_event: Optional[TDEventOperationTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_ref
        if self.operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event
        if self.td_event is not None:
            serialized = SerializationHelper.serialize_item(self.td_event, "TDEventOperationTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOperation":
        """Deserialize XML element to TDEventOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventOperation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATION-REF":
                setattr(obj, "operation_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT":
                setattr(obj, "td_event", TDEventOperationTypeEnum.deserialize(child))

        return obj



class TDEventOperationBuilder(TDEventVfbPortBuilder):
    """Builder for TDEventOperation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventOperation = TDEventOperation()


    def with_operation(self, value: Optional[ClientServerOperation]) -> "TDEventOperationBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'operation' is required and cannot be None")
        self._obj.operation = value
        return self

    def with_td_event(self, value: Optional[TDEventOperationTypeEnum]) -> "TDEventOperationBuilder":
        """Set td_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'td_event' is required and cannot be None")
        self._obj.td_event = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "operation",
        "tdEvent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventOperation:
        """Build and return the TDEventOperation instance with validation."""
        self._validate_instance()
        return self._obj