"""BswModuleEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 32)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 976)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 216)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 431)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 171)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswExecutionContext,
)
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import (
    SwServiceImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_arg import (
        SwServiceArg,
    )



class BswModuleEntry(ARElement):
    """AUTOSAR BswModuleEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[SwServiceArg]
    bsw_entry_kind_enum: Optional[BswEntryKindEnum]
    call_type: Optional[BswCallType]
    execution: Optional[BswExecutionContext]
    function: Optional[NameToken]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    return_type: Optional[SwServiceArg]
    role: Optional[Identifier]
    service_id: Optional[PositiveInteger]
    sw_service_impl_policy: Optional[SwServiceImplPolicyEnum]
    def __init__(self) -> None:
        """Initialize BswModuleEntry."""
        super().__init__()
        self.arguments: list[SwServiceArg] = []
        self.bsw_entry_kind_enum: Optional[BswEntryKindEnum] = None
        self.call_type: Optional[BswCallType] = None
        self.execution: Optional[BswExecutionContext] = None
        self.function: Optional[NameToken] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None
        self.return_type: Optional[SwServiceArg] = None
        self.role: Optional[Identifier] = None
        self.service_id: Optional[PositiveInteger] = None
        self.sw_service_impl_policy: Optional[SwServiceImplPolicyEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleEntry":
        """Deserialize XML element to BswModuleEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleEntry, cls).deserialize(element)

        # Parse arguments (list from container "ARGUMENTS")
        obj.arguments = []
        container = ARObject._find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.arguments.append(child_value)

        # Parse bsw_entry_kind_enum
        child = ARObject._find_child_element(element, "BSW-ENTRY-KIND-ENUM")
        if child is not None:
            bsw_entry_kind_enum_value = BswEntryKindEnum.deserialize(child)
            obj.bsw_entry_kind_enum = bsw_entry_kind_enum_value

        # Parse call_type
        child = ARObject._find_child_element(element, "CALL-TYPE")
        if child is not None:
            call_type_value = BswCallType.deserialize(child)
            obj.call_type = call_type_value

        # Parse execution
        child = ARObject._find_child_element(element, "EXECUTION")
        if child is not None:
            execution_value = BswExecutionContext.deserialize(child)
            obj.execution = execution_value

        # Parse function
        child = ARObject._find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        # Parse is_reentrant
        child = ARObject._find_child_element(element, "IS-REENTRANT")
        if child is not None:
            is_reentrant_value = child.text
            obj.is_reentrant = is_reentrant_value

        # Parse is_synchronous
        child = ARObject._find_child_element(element, "IS-SYNCHRONOUS")
        if child is not None:
            is_synchronous_value = child.text
            obj.is_synchronous = is_synchronous_value

        # Parse return_type
        child = ARObject._find_child_element(element, "RETURN-TYPE")
        if child is not None:
            return_type_value = ARObject._deserialize_by_tag(child, "SwServiceArg")
            obj.return_type = return_type_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse service_id
        child = ARObject._find_child_element(element, "SERVICE-ID")
        if child is not None:
            service_id_value = child.text
            obj.service_id = service_id_value

        # Parse sw_service_impl_policy
        child = ARObject._find_child_element(element, "SW-SERVICE-IMPL-POLICY")
        if child is not None:
            sw_service_impl_policy_value = SwServiceImplPolicyEnum.deserialize(child)
            obj.sw_service_impl_policy = sw_service_impl_policy_value

        return obj



class BswModuleEntryBuilder:
    """Builder for BswModuleEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleEntry = BswModuleEntry()

    def build(self) -> BswModuleEntry:
        """Build and return BswModuleEntry object.

        Returns:
            BswModuleEntry instance
        """
        # TODO: Add validation
        return self._obj
