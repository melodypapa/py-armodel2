"""SecurityEventContextMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)
from abc import ABC, abstractmethod


class SecurityEventContextMapping(IdsMapping, ABC):
    """AUTOSAR SecurityEventContextMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    filter_chain_ref: Optional[Any]
    idsm_instance_ref: Optional[ARRef]
    _mapped_securities: list[Any]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain_ref: Optional[Any] = None
        self.idsm_instance_ref: Optional[ARRef] = None
        self._mapped_securities: list[Any] = []
    @property
    @xml_element_name("MAPPED-SECURITYS")
    def mapped_securities(self) -> list[Any]:
        """Get mapped_securities with custom XML element name."""
        return self._mapped_securities

    @mapped_securities.setter
    def mapped_securities(self, value: list[Any]) -> None:
        """Set mapped_securities with custom XML element name."""
        self._mapped_securities = value


    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize filter_chain_ref
        if self.filter_chain_ref is not None:
            serialized = SerializationHelper.serialize_item(self.filter_chain_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-CHAIN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize idsm_instance_ref
        if self.idsm_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.idsm_instance_ref, "IdsmInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_securities (list to container "MAPPED-SECURITYS")
        if self.mapped_securities:
            wrapper = ET.Element("MAPPED-SECURITYS")
            for item in self.mapped_securities:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMapping":
        """Deserialize XML element to SecurityEventContextMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMapping, cls).deserialize(element)

        # Parse filter_chain_ref
        child = SerializationHelper.find_child_element(element, "FILTER-CHAIN-REF")
        if child is not None:
            filter_chain_ref_value = ARRef.deserialize(child)
            obj.filter_chain_ref = filter_chain_ref_value

        # Parse idsm_instance_ref
        child = SerializationHelper.find_child_element(element, "IDSM-INSTANCE-REF")
        if child is not None:
            idsm_instance_ref_value = ARRef.deserialize(child)
            obj.idsm_instance_ref = idsm_instance_ref_value

        # Parse mapped_securities (list from container "MAPPED-SECURITYS")
        obj.mapped_securities = []
        container = SerializationHelper.find_child_element(element, "MAPPED-SECURITYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapped_securities.append(child_value)

        return obj



