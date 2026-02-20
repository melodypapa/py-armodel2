"""SenderReceiverInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 335)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 94)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2054)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 244)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.invalidation_policy import (
    InvalidationPolicy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item_set import (
    MetaDataItemSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverInterface(DataInterface):
    """AUTOSAR SenderReceiverInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_elements: list[VariableDataPrototype]
    invalidation_policy_policies: list[InvalidationPolicy]
    meta_data_item_sets: list[MetaDataItemSet]
    def __init__(self) -> None:
        """Initialize SenderReceiverInterface."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []
        self.invalidation_policy_policies: list[InvalidationPolicy] = []
        self.meta_data_item_sets: list[MetaDataItemSet] = []

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_elements (list to container "DATA-ELEMENTS")
        if self.data_elements:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_elements:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize invalidation_policy_policies (list to container "INVALIDATION-POLICY-POLICIES")
        if self.invalidation_policy_policies:
            wrapper = ET.Element("INVALIDATION-POLICY-POLICIES")
            for item in self.invalidation_policy_policies:
                serialized = ARObject._serialize_item(item, "InvalidationPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize meta_data_item_sets (list to container "META-DATA-ITEM-SETS")
        if self.meta_data_item_sets:
            wrapper = ET.Element("META-DATA-ITEM-SETS")
            for item in self.meta_data_item_sets:
                serialized = ARObject._serialize_item(item, "MetaDataItemSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverInterface":
        """Deserialize XML element to SenderReceiverInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverInterface, cls).deserialize(element)

        # Parse data_elements (list from container "DATA-ELEMENTS")
        obj.data_elements = []
        container = ARObject._find_child_element(element, "DATA-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_elements.append(child_value)

        # Parse invalidation_policy_policies (list from container "INVALIDATION-POLICY-POLICIES")
        obj.invalidation_policy_policies = []
        container = ARObject._find_child_element(element, "INVALIDATION-POLICY-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.invalidation_policy_policies.append(child_value)

        # Parse meta_data_item_sets (list from container "META-DATA-ITEM-SETS")
        obj.meta_data_item_sets = []
        container = ARObject._find_child_element(element, "META-DATA-ITEM-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.meta_data_item_sets.append(child_value)

        return obj



class SenderReceiverInterfaceBuilder:
    """Builder for SenderReceiverInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverInterface = SenderReceiverInterface()

    def build(self) -> SenderReceiverInterface:
        """Build and return SenderReceiverInterface object.

        Returns:
            SenderReceiverInterface instance
        """
        # TODO: Add validation
        return self._obj
