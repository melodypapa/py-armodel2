"""GlobalTimeMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeIcvSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = ARObject._serialize_item(self.communication_connector_ref, "CommunicationConnector")
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
            serialized = ARObject._serialize_item(self.icv_secured, "GlobalTimeIcvSupportEnum")
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
            serialized = ARObject._serialize_item(self.immediate, "TimeValue")
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
            serialized = ARObject._serialize_item(self.is_system_wide, "Boolean")
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
            serialized = ARObject._serialize_item(self.sync_period, "TimeValue")
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

        # Parse communication_connector_ref
        child = ARObject._find_child_element(element, "COMMUNICATION-CONNECTOR-REF")
        if child is not None:
            communication_connector_ref_value = ARRef.deserialize(child)
            obj.communication_connector_ref = communication_connector_ref_value

        # Parse icv_secured
        child = ARObject._find_child_element(element, "ICV-SECURED")
        if child is not None:
            icv_secured_value = GlobalTimeIcvSupportEnum.deserialize(child)
            obj.icv_secured = icv_secured_value

        # Parse immediate
        child = ARObject._find_child_element(element, "IMMEDIATE")
        if child is not None:
            immediate_value = child.text
            obj.immediate = immediate_value

        # Parse is_system_wide
        child = ARObject._find_child_element(element, "IS-SYSTEM-WIDE")
        if child is not None:
            is_system_wide_value = child.text
            obj.is_system_wide = is_system_wide_value

        # Parse sync_period
        child = ARObject._find_child_element(element, "SYNC-PERIOD")
        if child is not None:
            sync_period_value = child.text
            obj.sync_period = sync_period_value

        return obj



class GlobalTimeMasterBuilder:
    """Builder for GlobalTimeMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeMaster = GlobalTimeMaster()

    def build(self) -> GlobalTimeMaster:
        """Build and return GlobalTimeMaster object.

        Returns:
            GlobalTimeMaster instance
        """
        # TODO: Add validation
        return self._obj
