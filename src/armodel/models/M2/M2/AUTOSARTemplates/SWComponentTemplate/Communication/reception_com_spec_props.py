"""ReceptionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ReceptionComSpecProps(ARObject):
    """AUTOSAR ReceptionComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_update": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataUpdate
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
    }

    def __init__(self) -> None:
        """Initialize ReceptionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.timeout: Optional[TimeValue] = None


class ReceptionComSpecPropsBuilder:
    """Builder for ReceptionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceptionComSpecProps = ReceptionComSpecProps()

    def build(self) -> ReceptionComSpecProps:
        """Build and return ReceptionComSpecProps object.

        Returns:
            ReceptionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
