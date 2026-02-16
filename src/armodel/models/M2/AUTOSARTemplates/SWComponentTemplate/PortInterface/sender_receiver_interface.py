"""SenderReceiverInterface AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # dataElements
        "invalidation_policy_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InvalidationPolicy,
        ),  # invalidationPolicyPolicies
        "meta_data_item_sets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MetaDataItemSet,
        ),  # metaDataItemSets
    }

    def __init__(self) -> None:
        """Initialize SenderReceiverInterface."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []
        self.invalidation_policy_policies: list[InvalidationPolicy] = []
        self.meta_data_item_sets: list[MetaDataItemSet] = []


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
