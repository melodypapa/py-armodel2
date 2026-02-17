"""MacSecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_local_kay_props import (
    MacSecLocalKayProps,
)


class MacSecProps(ARObject):
    """AUTOSAR MacSecProps."""

    auto_start: Optional[Boolean]
    mac_sec_kay: Optional[MacSecLocalKayProps]
    on_fail: Optional[TimeValue]
    sak_rekey_time: Optional[TimeValue]
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
