"""BswModuleEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, SwServiceArg),  # arguments
        ("bsw_entry_kind_enum", None, False, False, BswEntryKindEnum),  # bswEntryKindEnum
        ("call_type", None, False, False, BswCallType),  # callType
        ("execution", None, False, False, BswExecutionContext),  # execution
        ("function", None, True, False, None),  # function
        ("is_reentrant", None, True, False, None),  # isReentrant
        ("is_synchronous", None, True, False, None),  # isSynchronous
        ("return_type", None, False, False, SwServiceArg),  # returnType
        ("role", None, True, False, None),  # role
        ("service_id", None, True, False, None),  # serviceId
        ("sw_service_impl_policy", None, False, False, SwServiceImplPolicyEnum),  # swServiceImplPolicy
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleEntry":
        """Create BswModuleEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleEntry since parent returns ARObject
        return cast("BswModuleEntry", obj)


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
