"""IPdu AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)


class IPdu(Pdu):
    """AUTOSAR IPdu."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "contained_i_pdu_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ContainedIPduProps,
        ),  # containedIPduProps
    }

    def __init__(self) -> None:
        """Initialize IPdu."""
        super().__init__()
        self.contained_i_pdu_props: Optional[ContainedIPduProps] = None


class IPduBuilder:
    """Builder for IPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPdu = IPdu()

    def build(self) -> IPdu:
        """Build and return IPdu object.

        Returns:
            IPdu instance
        """
        # TODO: Add validation
        return self._obj
