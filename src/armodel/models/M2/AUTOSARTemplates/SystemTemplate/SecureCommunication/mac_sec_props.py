"""MacSecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_local_kay_props import (
    MacSecLocalKayProps,
)


class MacSecProps(ARObject):
    """AUTOSAR MacSecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "auto_start": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # autoStart
        "mac_sec_kay": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecLocalKayProps,
        ),  # macSecKay
        "on_fail": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # onFail
        "sak_rekey_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sakRekeyTime
    }

    def __init__(self) -> None:
        """Initialize MacSecProps."""
        super().__init__()
        self.auto_start: Optional[Boolean] = None
        self.mac_sec_kay: Optional[MacSecLocalKayProps] = None
        self.on_fail: Optional[TimeValue] = None
        self.sak_rekey_time: Optional[TimeValue] = None


class MacSecPropsBuilder:
    """Builder for MacSecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecProps = MacSecProps()

    def build(self) -> MacSecProps:
        """Build and return MacSecProps object.

        Returns:
            MacSecProps instance
        """
        # TODO: Add validation
        return self._obj
