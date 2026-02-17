"""Fibex4Multiplatform module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.gateway import (
        Gateway,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
        FrameMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
        IPduMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.target_i_pdu_ref import (
        TargetIPduRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
        PduMappingDefaultValue,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
        DefaultValueElement,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
        ISignalMapping,
    )

__all__ = [
    "DefaultValueElement",
    "FrameMapping",
    "Gateway",
    "IPduMapping",
    "ISignalMapping",
    "PduMappingDefaultValue",
    "TargetIPduRef",
]
