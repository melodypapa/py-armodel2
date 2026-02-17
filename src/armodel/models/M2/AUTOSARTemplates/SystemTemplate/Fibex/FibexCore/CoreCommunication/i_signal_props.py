"""ISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ISignalProps(ARObject):
    """AUTOSAR ISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "handle_out_of_range": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (HandleOutOfRange),
        ),  # handleOutOfRange
    }

    def __init__(self) -> None:
        """Initialize ISignalProps."""
        super().__init__()
        self.handle_out_of_range: Optional[Any] = None


class ISignalPropsBuilder:
    """Builder for ISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalProps = ISignalProps()

    def build(self) -> ISignalProps:
        """Build and return ISignalProps object.

        Returns:
            ISignalProps instance
        """
        # TODO: Add validation
        return self._obj
