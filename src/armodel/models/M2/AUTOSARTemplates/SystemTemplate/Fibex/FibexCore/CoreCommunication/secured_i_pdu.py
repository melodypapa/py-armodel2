"""SecuredIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 367)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[Any]
    dynamic: Optional[Boolean]
    freshness_props: Optional[Any]
    payload: Optional[PduTriggering]
    secure: Optional[Any]
    use_as: Optional[Boolean]
    use_secured_pdu: Optional[SecuredPduHeaderEnum]
    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props: Optional[Any] = None
        self.payload: Optional[PduTriggering] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None


class SecuredIPduBuilder:
    """Builder for SecuredIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecuredIPdu = SecuredIPdu()

    def build(self) -> SecuredIPdu:
        """Build and return SecuredIPdu object.

        Returns:
            SecuredIPdu instance
        """
        # TODO: Add validation
        return self._obj
