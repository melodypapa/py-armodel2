"""CanGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR CanGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fup_data_id_list: PositiveInteger
    ofns_data_id_list: PositiveInteger
    ofs_data_id_list: PositiveInteger
    sync_data_id_list: PositiveInteger
    def __init__(self) -> None:
        """Initialize CanGlobalTimeDomainProps."""
        super().__init__()
        self.fup_data_id_list: PositiveInteger = None
        self.ofns_data_id_list: PositiveInteger = None
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None
    def serialize(self) -> ET.Element:
        """Serialize CanGlobalTimeDomainProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanGlobalTimeDomainProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fup_data_id_list
        if self.fup_data_id_list is not None:
            serialized = ARObject._serialize_item(self.fup_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUP-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ofns_data_id_list
        if self.ofns_data_id_list is not None:
            serialized = ARObject._serialize_item(self.ofns_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFNS-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ofs_data_id_list
        if self.ofs_data_id_list is not None:
            serialized = ARObject._serialize_item(self.ofs_data_id_list, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.sync_data_id_list, "PositiveInteger")
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
    def deserialize(cls, element: ET.Element) -> "CanGlobalTimeDomainProps":
        """Deserialize XML element to CanGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanGlobalTimeDomainProps, cls).deserialize(element)

        # Parse fup_data_id_list
        child = ARObject._find_child_element(element, "FUP-DATA-ID-LIST")
        if child is not None:
            fup_data_id_list_value = child.text
            obj.fup_data_id_list = fup_data_id_list_value

        # Parse ofns_data_id_list
        child = ARObject._find_child_element(element, "OFNS-DATA-ID-LIST")
        if child is not None:
            ofns_data_id_list_value = child.text
            obj.ofns_data_id_list = ofns_data_id_list_value

        # Parse ofs_data_id_list
        child = ARObject._find_child_element(element, "OFS-DATA-ID-LIST")
        if child is not None:
            ofs_data_id_list_value = child.text
            obj.ofs_data_id_list = ofs_data_id_list_value

        # Parse sync_data_id_list
        child = ARObject._find_child_element(element, "SYNC-DATA-ID-LIST")
        if child is not None:
            sync_data_id_list_value = child.text
            obj.sync_data_id_list = sync_data_id_list_value

        return obj



class CanGlobalTimeDomainPropsBuilder:
    """Builder for CanGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanGlobalTimeDomainProps = CanGlobalTimeDomainProps()

    def build(self) -> CanGlobalTimeDomainProps:
        """Build and return CanGlobalTimeDomainProps object.

        Returns:
            CanGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
