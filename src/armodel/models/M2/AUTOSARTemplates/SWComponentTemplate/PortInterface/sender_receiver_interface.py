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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_element_refs (list)
        obj.data_element_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-ELEMENTS"):
            data_element_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_refs.append(data_element_refs_value)

        # Parse invalidation_policy_policies (list)
        obj.invalidation_policy_policies = []
        for child in ARObject._find_all_child_elements(element, "INVALIDATION-POLICY-POLICIES"):
            invalidation_policy_policies_value = ARObject._deserialize_by_tag(child, "InvalidationPolicy")
            obj.invalidation_policy_policies.append(invalidation_policy_policies_value)

        # Parse meta_data_item_set_refs (list)
        obj.meta_data_item_set_refs = []
        for child in ARObject._find_all_child_elements(element, "META-DATA-ITEM-SETS"):
            meta_data_item_set_refs_value = ARObject._deserialize_by_tag(child, "MetaDataItemSet")
            obj.meta_data_item_set_refs.append(meta_data_item_set_refs_value)

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
