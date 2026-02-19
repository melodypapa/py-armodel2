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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    data_element_refs: list[ARRef]
    invalidation_policy_policies: list[InvalidationPolicy]
    meta_data_item_set_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SenderReceiverInterface."""
        super().__init__()
        self.data_element_refs: list[ARRef] = []
        self.invalidation_policy_policies: list[InvalidationPolicy] = []
        self.meta_data_item_set_refs: list[ARRef] = []
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

        # Parse data_element_refs (list from container "DATA-ELEMENTS")
        obj.data_element_refs = []
        container = ARObject._find_child_element(element, "DATA-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_element_refs.append(child_value)

        # Parse invalidation_policy_policies (list from container "INVALIDATION-POLICY-POLICIES")
        obj.invalidation_policy_policies = []
        container = ARObject._find_child_element(element, "INVALIDATION-POLICY-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.invalidation_policy_policies.append(child_value)

        # Parse meta_data_item_set_refs (list from container "META-DATA-ITEM-SETS")
        obj.meta_data_item_set_refs = []
        container = ARObject._find_child_element(element, "META-DATA-ITEM-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.meta_data_item_set_refs.append(child_value)

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
