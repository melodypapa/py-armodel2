"""DynamicPartAlternative AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_dynamic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialDynamic
        "i_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalIPdu,
        ),  # iPdu
        "selector_field": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # selectorField
    }

    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu: Optional[ISignalIPdu] = None
        self.selector_field: Optional[Integer] = None


class DynamicPartAlternativeBuilder:
    """Builder for DynamicPartAlternative."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPartAlternative = DynamicPartAlternative()

    def build(self) -> DynamicPartAlternative:
        """Build and return DynamicPartAlternative object.

        Returns:
            DynamicPartAlternative instance
        """
        # TODO: Add validation
        return self._obj
