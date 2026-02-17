"""IEEE1722TpAv module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_crf_connection import (
        IEEE1722TpCrfConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_aaf_connection import (
        IEEE1722TpAafConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_iidc_connection import (
        IEEE1722TpIidcConnection,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_rvf_connection import (
        IEEE1722TpRvfConnection,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_crf_type_enum import (
    IEEE1722TpCrfTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_crf_pull_enum import (
    IEEE1722TpCrfPullEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_aaf_nominal_rate_enum import (
    IEEE1722TpAafNominalRateEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_aaf_format_enum import (
    IEEE1722TpAafFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_aaf_aes3_data_type_enum import (
    IEEE1722TpAafAes3DataTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_rvf_pixel_depth_enum import (
    IEEE1722TpRvfPixelDepthEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_rvf_pixel_format_enum import (
    IEEE1722TpRvfPixelFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_rvf_color_space_enum import (
    IEEE1722TpRvfColorSpaceEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv.ieee1722_tp_rvf_frame_rate_enum import (
    IEEE1722TpRvfFrameRateEnum,
)

__all__ = [
    "IEEE1722TpAafAes3DataTypeEnum",
    "IEEE1722TpAafConnection",
    "IEEE1722TpAafFormatEnum",
    "IEEE1722TpAafNominalRateEnum",
    "IEEE1722TpCrfConnection",
    "IEEE1722TpCrfPullEnum",
    "IEEE1722TpCrfTypeEnum",
    "IEEE1722TpIidcConnection",
    "IEEE1722TpRvfColorSpaceEnum",
    "IEEE1722TpRvfConnection",
    "IEEE1722TpRvfFrameRateEnum",
    "IEEE1722TpRvfPixelDepthEnum",
    "IEEE1722TpRvfPixelFormatEnum",
]
