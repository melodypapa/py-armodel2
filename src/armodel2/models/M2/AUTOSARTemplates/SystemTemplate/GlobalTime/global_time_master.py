"""GlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeIcvSupportEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeMaster(Identifiable, ABC):
    """AUTOSAR GlobalTimeMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector_ref: Optional[ARRef]
    icv_secured: Optional[GlobalTimeIcvSupportEnum]
    immediate: Optional[TimeValue]
    is_system_wide: Optional[Boolean]
    sync_period: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION-CONNECTOR-REF": ("_POLYMORPHIC", "communication_connector_ref", ["AbstractCanCommunicationConnector", "CanCommunicationConnector", "EthernetCommunicationConnector", "FlexrayCommunicationConnector", "LinCommunicationConnector", "TtcanCommunicationConnector", "UserDefinedCommunicationConnector"]),
        "ICV-SECURED": lambda obj, elem: setattr(obj, "icv_secured", GlobalTimeIcvSupportEnum.deserialize(elem)),
        "IMMEDIATE": lambda obj, elem: setattr(obj, "immediate", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "IS-SYSTEM-WIDE": lambda obj, elem: setattr(obj, "is_system_wide", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SYNC-PERIOD": lambda obj, elem: setattr(obj, "sync_period", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeMaster."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.icv_secured: Optional[GlobalTimeIcvSupportEnum] = None
        self.immediate: Optional[TimeValue] = None
        self.is_system_wide: Optional[Boolean] = None
        self.sync_period: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_connector_ref, "CommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize icv_secured
        if self.icv_secured is not None:
            serialized = SerializationHelper.serialize_item(self.icv_secured, "GlobalTimeIcvSupportEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ICV-SECURED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize immediate
        if self.immediate is not None:
            serialized = SerializationHelper.serialize_item(self.immediate, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMMEDIATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_system_wide
        if self.is_system_wide is not None:
            serialized = SerializationHelper.serialize_item(self.is_system_wide, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SYSTEM-WIDE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_period
        if self.sync_period is not None:
            serialized = SerializationHelper.serialize_item(self.sync_period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeMaster":
        """Deserialize XML element to GlobalTimeMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeMaster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION-CONNECTOR-REF":
                setattr(obj, "communication_connector_ref", ARRef.deserialize(child))
            elif tag == "ICV-SECURED":
                setattr(obj, "icv_secured", GlobalTimeIcvSupportEnum.deserialize(child))
            elif tag == "IMMEDIATE":
                setattr(obj, "immediate", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "IS-SYSTEM-WIDE":
                setattr(obj, "is_system_wide", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SYNC-PERIOD":
                setattr(obj, "sync_period", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class GlobalTimeMasterBuilder(IdentifiableBuilder):
    """Builder for GlobalTimeMaster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeMaster = GlobalTimeMaster()


    def with_communication_connector(self, value: Optional[CommunicationConnector]) -> "GlobalTimeMasterBuilder":
        """Set communication_connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'communication_connector' is required and cannot be None")
        self._obj.communication_connector = value
        return self

    def with_icv_secured(self, value: Optional[GlobalTimeIcvSupportEnum]) -> "GlobalTimeMasterBuilder":
        """Set icv_secured attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'icv_secured' is required and cannot be None")
        self._obj.icv_secured = value
        return self

    def with_immediate(self, value: Optional[TimeValue]) -> "GlobalTimeMasterBuilder":
        """Set immediate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'immediate' is required and cannot be None")
        self._obj.immediate = value
        return self

    def with_is_system_wide(self, value: Optional[Boolean]) -> "GlobalTimeMasterBuilder":
        """Set is_system_wide attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_system_wide' is required and cannot be None")
        self._obj.is_system_wide = value
        return self

    def with_sync_period(self, value: Optional[TimeValue]) -> "GlobalTimeMasterBuilder":
        """Set sync_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sync_period' is required and cannot be None")
        self._obj.sync_period = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "communicationConnector",
        "icvSecured",
        "immediate",
        "isSystemWide",
        "syncPeriod",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> GlobalTimeMaster:
        """Build and return the GlobalTimeMaster instance (abstract)."""
        raise NotImplementedError