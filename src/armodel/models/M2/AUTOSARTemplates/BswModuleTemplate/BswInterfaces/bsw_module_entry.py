"""BswModuleEntry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
)
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_arg import (
    SwServiceArg,
)


class BswModuleEntry(ARElement):
    """AUTOSAR BswModuleEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwServiceArg,
        ),  # arguments
        "bsw_entry_kind_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswEntryKindEnum,
        ),  # bswEntryKindEnum
        "call_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswCallType,
        ),  # callType
        "execution": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswExecutionContext,
        ),  # execution
        "function": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # function
        "is_reentrant": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isReentrant
        "is_synchronous": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isSynchronous
        "return_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwServiceArg,
        ),  # returnType
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "service_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # serviceId
        "sw_service_impl_policy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwServiceImplPolicyEnum,
        ),  # swServiceImplPolicy
    }

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
